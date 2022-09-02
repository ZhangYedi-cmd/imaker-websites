package com.zhang.controller;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.zhang.constans.GenderConstants;
import com.zhang.exception.BusinessException;
import com.zhang.model.entity.User;
import com.zhang.model.enums.ErrorCodeEnum;
import com.zhang.service.UserService;
import com.zhang.untils.CaptchaUtils;
import org.apache.commons.lang3.StringUtils;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;
import javax.xml.crypto.Data;
import java.util.Date;

@RestController
public class CaptchaController {

  @Resource
  private UserService userService;

  /**
   * 获取验证码
   */
  @GetMapping("/captcha")
  public String getCaptcha(
      String mpOpenId,
      String nickName,
      Integer gender,
      String avatarUrl
  ) {
    if (StringUtils.isAnyBlank(mpOpenId)) {
      throw new BusinessException(ErrorCodeEnum.REQUEST_PARAMS_ERROR);
    }
    String captchaCode = CaptchaUtils.getCaptchaCode();
    QueryWrapper<User> wrapper = new QueryWrapper<>();
    wrapper.like("openId", mpOpenId);
    User temUser = userService.getOne(wrapper);
    if (temUser == null) {
      String count = String.valueOf(userService.count());
      temUser = new User();
      temUser.setUsername("鸭鸭" + count + "号");
      temUser.setOpenId(mpOpenId);
      temUser.setAvatarUrl(avatarUrl);
      temUser.setNickName(nickName);
      temUser.setGender(GenderConstants.MAN == gender ? gender : GenderConstants.WOMAN);
      temUser.setCaptcha(captchaCode);
      userService.save(temUser);
      return captchaCode;
    }
    temUser.setCaptcha(captchaCode);
    temUser.setCaptchaTime(new Date());
    userService.updateById(temUser);
    return captchaCode;
  }
}
