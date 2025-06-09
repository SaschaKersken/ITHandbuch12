import java.util.List;
import java.lang.Math;

public class StreamTest {
    public static void main(String[] args) {
        var numbers = List.of(-3, -1, 0, 2, 4);
        System.out.println("Originalliste:");
        System.out.println(numbers);
        System.out.println("Die ersten drei Zahlen:");
        numbers
            .stream()
            .limit(3)
            .forEach(number -> System.out.println(number));
        System.out.println("Nur die positiven Zahlen:");
        numbers
            .stream()
            .filter(number -> number > 0)
            .forEach(number -> System.out.println(number));
        System.out.println("Das Doppelte jeder Zahl:");
        numbers
            .stream()
            .map(number -> number * 2)
            .forEach(number-> System.out.println(number));
        System.out.println("Summe der Beträge:");
        System.out.println(numbers
            .stream()
            .reduce(0, (total, number) -> total + Math.abs(number))
        );
    }
}
