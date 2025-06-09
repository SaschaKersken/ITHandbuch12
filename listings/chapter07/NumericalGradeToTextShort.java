public class NumericalGradeToTextShort {
    public static void main(String args[]) {
        if (args.length >= 1) {
            int grade = 0;
            try {
                grade = Integer.parseInt(args[0]);
            } catch(NumberFormatException e) {
                System.out.println("Die Note muss eine Zahl sein.");
                System.exit(1);
            }
            System.out.println(
                switch(grade) {
                    case 6 -> "Ungenügend";
                    case 5 -> "Mangelhaft";
                    case 4 -> "Ausreichend";
                    case 3 -> "Befriedigend";
                    case 2 -> "Gut";
                    case 1 -> "Sehr gut";
                    default -> "Keine gültige Note.";
                }
            );
        } else {
            System.out.println("Verwendung: java NumericalGradeToTextShort NOTE");
        }
    }
}

