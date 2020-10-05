package com.demo;

@Options("Class")
public class Demo {
    @Options("Field")
    public int x;
    private String y;

    @Options("Constructor")
    public Demo() {
    }

    public Demo(int x, String y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }

    @Options("Method")
    public int add(int a, String b) {
        return a + Integer.parseInt(b);
    }

    @Override
    public String toString() {
        return "Demo{" +
                "x=" + x +
                ", y='" + y + '\'' +
                '}';
    }
}
