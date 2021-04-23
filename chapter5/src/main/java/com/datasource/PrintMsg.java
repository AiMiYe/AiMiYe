package com.datasource;

public class PrintMsg {
    public static void main(String[] args) {
        for (; ; ) {
            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("msg");
        }
    }
}
