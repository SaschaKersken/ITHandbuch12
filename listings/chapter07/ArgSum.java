import java.util.stream.Stream;

public class ArgSum {
    public static void main(String[] args) {
        try {
            System.out.println(
                Stream.of(args)
                    .map(Integer::parseInt)
                    .reduce(0, (sum, number) -> sum += number)
            );
        } catch(NumberFormatException e) {
            System.out.println("Bitte nur Zahlen eingeben. " + e.getMessage());
        }
    }
}
