package assignment_2;

public class ShapeTest {
    public static void main(String[] args) {
        Shape[] shapes = new Shape[4];

        shapes[0] = new Circle(5);
        shapes[1] = new Square(4);
        shapes[2] = new Sphere(3);
        shapes[3] = new Cube(2);

        for (Shape shape : shapes) {
            System.out.println(shape.toString());
            System.out.printf("Area: %.2f%n", shape.getArea());
            if (shape instanceof ThreeDimensionalShape) {
                ThreeDimensionalShape threeDShape = (ThreeDimensionalShape) shape;
                System.out.printf("Volume: %.2f%n", threeDShape.getVolume());
            }
            System.out.println();
        }
    }
}
