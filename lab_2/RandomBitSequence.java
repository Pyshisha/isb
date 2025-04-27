import java.util.Random;

public class RandomBitSequence {
    public static void main(String[] args) {
        Random random = new Random(System.currentTimeMillis()); // Инициализация сида по времени

        StringBuilder sequence = new StringBuilder();

        for (int i = 0; i < 128; i++) {
            int bit = random.nextInt(2); // Генерируем 0 или 1
            sequence.append(bit);
        }

        System.out.println(sequence.toString());
    }
}