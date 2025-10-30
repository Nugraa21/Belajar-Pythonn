package python;

import java.util.Scanner;

public class JenisSegitiga {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Menentukan Jenis Segitiga" );
        System.out.print("Masukkan sisi pertama: ");
        double a = input.nextDouble();

        System.out.print("Masukkan sisi kedua: ");
        double b = input.nextDouble();

        System.out.print("Masukkan sisi ketiga: ");
        double c = input.nextDouble();

        if (a + b > c && a + c > b && b + c > a) {
            if (a == b && b == c) {
                System.out.println("Segitiga tersebut adalah Segitiga Sama Sisi.");
            } else if (a == b || a == c || b == c) {
                System.out.println("Segitiga tersebut adalah Segitiga Sama Kaki.");
            } else {
                System.out.println("Segitiga tersebut adalah Segitiga Sembarang.");
            }
        } else {
            System.out.println("Nilai sisi yang dimasukkan tidak dapat membentuk segitiga!");
        }

        input.close();
    }
}
