package com.chapter1.parameter;

import org.testng.Assert;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

public class ParameterTest {

    @Test
    @Parameters({"x", "y", "expected"})
    public void parameterTest(int x, int y, int expected) {
        int rlt = x + y;
        System.out.println(rlt);
        Assert.assertEquals(rlt, expected);
    }
}
