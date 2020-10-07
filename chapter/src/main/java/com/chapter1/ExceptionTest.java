package com.chapter1;

import org.testng.annotations.Test;

public class ExceptionTest {

    @Test(expectedExceptions = NullPointerException.class)
    public void nullPointerException(){
        throw new NullPointerException();
    }
}
