package com.zhang.untils;

import java.util.Random;

public class CaptchaUtils {

  public static String getCaptchaCode() {
    //1，用随机生成数方法，生成验证码
    Random yzm = new Random();                          //定义一个随机生成数技术，用来生成随机数
    String yzm2 = "";                                   //定义一个空的Atring变量用来接收生成的验证码
    for (int i = 0; i < 5; i++) {                       //循环5次每次生成一位，5位验证码
      int a = yzm.nextInt(3);                             //验证码包括数字、大小写字母组成
      switch (a) {                                          //a:    0       1       2
        case 0:                                         //      数字   小写字母   大写字母
          char s = (char) (yzm.nextInt(26) + 65);
          yzm2 = yzm2 + s;
          break;
        case 1:
          char s1 = (char) (yzm.nextInt(26) + 97);
          yzm2 = yzm2 + s1;
          break;
        case 2:
          int s2 = yzm.nextInt(10);
          yzm2 = yzm2 + s2;
          break;
      }
    }
    return yzm2;
  }

}
