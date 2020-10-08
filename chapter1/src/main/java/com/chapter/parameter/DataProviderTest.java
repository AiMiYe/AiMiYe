package com.chapter.parameter;

import org.testng.Assert;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

public class DataProviderTest {
    @Test(dataProvider = "data")
    public void dateProviderTest(int x, int y, int expected) {
        int rlt = x + y;
        System.out.println(rlt);
        Assert.assertEquals(rlt, expected);
    }

    @DataProvider(name = "data")
    public Object[][] dateProvider() {
        return new Object[][]{
                {1, 6, 7},
                {5, 7, 12},
                {4, 9, 13}
        };
    }
}
