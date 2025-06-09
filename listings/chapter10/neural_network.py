import math
import csv
import numpy as np
from random import shuffle

# Sigmoidfunktion als Aktivierungsfunktion
def sigmoid(x):
    try:
        return 1 / (1 + math.exp(-x))
    except OverflowError:
        return 0

# Künstliches neuronales Netzwerk
class NeuralNetwork:

    # Attribute:
    # - Anzahl Neuronen der Eingabeschicht
    # - Anzahl Neuronen der versteckten Schicht
    # - Anzahl Neuronen der Ausgabeschicht
    # - Lernrate (benannt)
    def __init__(self, i_neurons, h_neurons, o_neurons, learning_rate = 0.1):
        # Grundattribute initialisieren
        self.input_neurons = i_neurons
        self.hidden_neurons = h_neurons
        self.output_neurons = o_neurons
        self.learning_rate = learning_rate
        self.categories = []

        # Gewichte als Zufallswerte initialisieren
        self.input_to_hidden = np.random.rand(
            self.hidden_neurons, self.input_neurons
        ) - 0.5
        self.hidden_to_output = np.random.rand(
            self.output_neurons, self.hidden_neurons
        ) - 0.5
        # Aktivierungsfunktion für NumPy-Arrays
        self.activation = np.vectorize(sigmoid)

    # Daten vorbereiten
    # Attribute:
    # - Daten als zweidimensionale Liste
    # - Anteil, der als Testdaten abgespalten werden soll
    # - Kategorie in der letzten Spalte? Sonst in der ersten
    def prepare(self, data, test_ratio=0.1, last=True):
        if last:
            x = [line[0:-1] for line in data]
            y = [line[-1] for line in data]
        else:
            x = [line[1:] for line in data]
            y = [line[0] for line in data]
        # Feature-Skalierung (x)
        columns = np.array(x).transpose()
        x_scaled = []
        for column in columns:
            if min(column) == max(column):
                column = np.zeros(len(column))
            else:
                column = (column - min(column)) / (max(column) - min(column))
            x_scaled.append(column)
        x = np.array(x_scaled).transpose()
        # Kategorien extrahieren und als Attribut speichern
        y_values = list(set(y))
        self.categories = y_values
        # Verteilung auf Ausgabeneuronen (y)
        y_spread = []
        for y_i in y:
            current = np.zeros(len(y_values))
            current[y_values.index(y_i)] = 1
            y_spread.append(current)
        y_out = np.array(y_spread)
        separator = int(test_ratio * len(x))
        return x[:separator], y[:separator], x[separator:], y_out[separator:]

    # Ein einzelner Trainingsdurchgang
    # Attribute:
    # - Eingabedaten als zweidimensionale Liste/Array
    # - Zieldaten als auf Ausgabeneuronen verteilte Liste/Array
    def train(self, inputs, targets):
        # Daten ins richtige Format bringen
        inputs = np.array(inputs, ndmin = 2).transpose()
        targets = np.array(targets, ndmin = 2).transpose()
        # Matrixmultiplikation: Gewichte versteckte Schicht * Eingabe
        hidden_in = np.dot(self.input_to_hidden, inputs)
        # Aktivierungsfunktion anwenden
        hidden_out = self.activation(hidden_in)
        # Matrixmultiplikation: Gewichte Ausgabeschicht * Ergebnis versteckt
        output_in = np.dot(self.hidden_to_output, hidden_out)
        # Aktivierungsfunktion anwenden
        output_out = self.activation(output_in)
        # Die Fehler berechnen
        output_diff = targets - output_out
        hidden_diff = np.dot(self.hidden_to_output.transpose(), output_diff)
        # Die Gewichte mit Lernrate * Fehler anpassen
        self.hidden_to_output += (
            self.learning_rate *
            np.dot(
                (output_diff * output_out * (1.0 - output_out)),
                hidden_out.transpose()
            )
        )
        self.input_to_hidden += (
            self.learning_rate *
            np.dot(
                (hidden_diff * hidden_out * (1.0 * hidden_out)),
                inputs.transpose()
            )
        )

    # Vorhersage für eine Reihe von Testdaten
    # Attribute:
    # - Eingabedaten als zweidimensionale Liste/Array
    # - Vergleichsdaten (benannt, optional)
    def predict(self, inputs, targets = None):
        # Dieselben Schritte wie in train()
        inputs = np.array(inputs, ndmin = 2).transpose()
        hidden_in = np.dot(self.input_to_hidden, inputs)
        hidden_out = self.activation(hidden_in)
        output_in = np.dot(self.hidden_to_output, hidden_out)
        output_out = self.activation(output_in)
        # Ausgabewerte den Kategorien zuweisen
        outputs = output_out.transpose()
        result = []
        for output in outputs:
            result.append(
                self.categories[list(output).index(max(output))]
            )
        # Wenn keine Zielwerte vorhanden, Ergebnisliste zurückgeben
        if targets is None:
            return result
        # Ansonsten vergleichen und korrekte Vorhersagen zählen
        correct = 0
        for res, pred in zip(targets, result):
            if res == pred:
                correct += 1
        percent = correct / len(result) * 100
        return correct, percent


# Hauptprogramm
if __name__ == '__main__':
    with open('iris_nn.csv', 'r') as iris_file:
        reader = csv.reader(iris_file, quoting=csv.QUOTE_NONNUMERIC)
        irises = list(reader)
    shuffle(irises)
    network = NeuralNetwork(4, 12, 3, learning_rate = 0.2)
    x_test, y_test, x_train, y_train = network.prepare(
      irises, test_ratio=0.2
    )
    for i in range(200):
        network.train(x_train, y_train)
    correct, percent = network.predict(x_test, targets = y_test)
    print(f"{correct} korrekte Vorhersagen ({percent}%).")
