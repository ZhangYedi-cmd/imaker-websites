package com.zhang;

import com.zhang.exception.BusinessException;
import com.zhang.service.UserService;
import org.joda.time.DateTime;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringBootConfiguration;
import org.springframework.boot.test.context.SpringBootTest;

import javax.annotation.Resource;
import java.util.Date;
import java.util.Random;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


class UserBackendApplicationTests {

  @Test
  public void testLoginFunc() {
    System.out.println("ok");

    System.out.println(new Date().getTime());
  }
}
