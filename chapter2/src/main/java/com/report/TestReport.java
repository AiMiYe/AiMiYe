package com.report;

import org.testng.Assert;
import org.testng.Reporter;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

public class TestReport {
    @Test(dataProvider = "data")
    public void testAdd(int x, int y, int expected) {
        int rlt = x + y;
        Assert.assertEquals(rlt, expected);
    }

    @Test
    public void testLog(){
        Reporter.log("TestCase output logs.");
        throw new RuntimeException("TestCase throw new RuntimeException.");
    }

    @DataProvider(name = "data")
    public Object[][] dateProvider() {
        return new Object[][]{
                {4, 4, 8},
                {5, 6, 11},
                {5, 5, 5},
                {12, 21, 33},
                {6, 7, 13},
                {8, 1, 9},
                {3, 7, 10},
                {53, 2, 55}
        };
    }
}
