package python;
import java.util.*;

public class Program {
    private static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        int bil1, bil2, bil3;
        int terbesar, terkecil;

        System.out.println("Masukkan bilangan pertama: ");
        bil1 = input.nextInt();
        System.out.println("Masukkan bilangan kedua: ");
        bil2 = input.nextInt();
        System.out.println("Masukkan bilangan ketiga: ");
        bil3 = input.nextInt();
        terbesar = bil1;
        terkecil = bil1;
        if (bil2 > terbesar) {
            terbesar = bil2;
        }
        if (bil2 < terkecil) {
            terkecil = bil2;
        }
        if (bil3 > terbesar) {
            terbesar = bil3;
        }
        if (bil3 < terkecil) {
            terkecil = bil3;
        }
        System.out.println("Bilangan terbesar adalah: " + terbesar);
        System.out.println("Bilangan terkecil adalah: " + terkecil);
    }
}
