package com.zhang.model.entity;

import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import java.io.Serializable;
import java.util.Date;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 *
 * @TableName user
 */
@TableName(value ="user")
@Data
@NoArgsConstructor
public class User implements Serializable {
  /**
   * 用户id

   */
  @TableId(value = "id")
  private Long id;

  /**
   * 用户名

   */
  @TableField(value = "username")
  private String username;

  /**
   * 昵称

   */
  @TableField(value = "nickName")
  private String nickName;

  /**
   * 用户账号

   */
  @TableField(value = "userAccount")
  private String userAccount;

  /**
   * 用户密码

   */
  @TableField(value = "userPassword")
  private String userPassword;

  /**
   * 兴趣方向
   */
  @TableField(value = "direction")
  private String direction;

  /**
   * 自我介绍
   */
  @TableField(value = "introduction")
  private String introduction;

  /**
   * 性别

   */
  @TableField(value = "gender")
  private Integer gender;

  /**
   * 头像地址

   */
  @TableField(value = "avatarUrl")
  private String avatarUrl;

  /**
   * 电话号码

   */
  @TableField(value = "phone")
  private String phone;

  /**
   * 电话

   */
  @TableField(value = "email")
  private String email;

  /**
   * 用户状态

   */
  @TableField(value = "userStatus")
  private Integer userStatus;

  /**
   * 创建时间

   */
  @TableField(value = "createTime")
  private Date createTime;

  /**
   * 数据更新时间

   */
  @TableField(value = "updateTime")
  private Date updateTime;

  /**
   * 是否删除
   */
  @TableField(value = "isDelete")
  private Integer isDelete;

  /**
   * 盐

   */
  @TableField(value = "salt")
  private String salt;

  /**
   * 用户类型
   */
  @TableField(value = "role")
  private Integer role;

  /**
   * 微信openid
   */
  @TableField(value = "openId")
  private String openId;

  /**
   * 验证码
   */
  @TableField(value = "captcha")
  private String captcha;

  /**
   * 验证码生成时间
   */
  @TableField(value = "captchaTime")
  private Date captchaTime;

  @TableField(exist = false)
  private static final long serialVersionUID = 1L;


  public User(String username, String userAccount, String userPassword, String salt) {
    this.username = username;
    this.userAccount = userAccount;
    this.userPassword = userPassword;
    this.salt = salt;
  }

  /**
   * 脱敏处理
   */
  public void setSafeUser() {
    this.setUserPassword(null);
    this.setSalt(null);
    this.setRole(null);
    this.setUserStatus(null);
    this.setOpenId(null);
    this.setCaptcha(null);
    this.setCaptchaTime(null);
  }


  @Override
  public boolean equals(Object that) {
    if (this == that) {
      return true;
    }
    if (that == null) {
      return false;
    }
    if (getClass() != that.getClass()) {
      return false;
    }
    User other = (User) that;
    return (this.getId() == null ? other.getId() == null : this.getId().equals(other.getId()))
      && (this.getUsername() == null ? other.getUsername() == null : this.getUsername().equals(other.getUsername()))
      && (this.getNickName() == null ? other.getNickName() == null : this.getNickName().equals(other.getNickName()))
      && (this.getUserAccount() == null ? other.getUserAccount() == null : this.getUserAccount().equals(other.getUserAccount()))
      && (this.getUserPassword() == null ? other.getUserPassword() == null : this.getUserPassword().equals(other.getUserPassword()))
      && (this.getDirection() == null ? other.getDirection() == null : this.getDirection().equals(other.getDirection()))
      && (this.getIntroduction() == null ? other.getIntroduction() == null : this.getIntroduction().equals(other.getIntroduction()))
      && (this.getGender() == null ? other.getGender() == null : this.getGender().equals(other.getGender()))
      && (this.getAvatarUrl() == null ? other.getAvatarUrl() == null : this.getAvatarUrl().equals(other.getAvatarUrl()))
      && (this.getPhone() == null ? other.getPhone() == null : this.getPhone().equals(other.getPhone()))
      && (this.getEmail() == null ? other.getEmail() == null : this.getEmail().equals(other.getEmail()))
      && (this.getUserStatus() == null ? other.getUserStatus() == null : this.getUserStatus().equals(other.getUserStatus()))
      && (this.getCreateTime() == null ? other.getCreateTime() == null : this.getCreateTime().equals(other.getCreateTime()))
      && (this.getUpdateTime() == null ? other.getUpdateTime() == null : this.getUpdateTime().equals(other.getUpdateTime()))
      && (this.getIsDelete() == null ? other.getIsDelete() == null : this.getIsDelete().equals(other.getIsDelete()))
      && (this.getSalt() == null ? other.getSalt() == null : this.getSalt().equals(other.getSalt()))
      && (this.getRole() == null ? other.getRole() == null : this.getRole().equals(other.getRole()))
      && (this.getOpenId() == null ? other.getOpenId() == null : this.getOpenId().equals(other.getOpenId()))
      && (this.getCaptcha() == null ? other.getCaptcha() == null : this.getCaptcha().equals(other.getCaptcha()))
      && (this.getCaptchaTime() == null ? other.getCaptchaTime() == null : this.getCaptchaTime().equals(other.getCaptchaTime()));
  }

  @Override
  public int hashCode() {
    final int prime = 31;
    int result = 1;
    result = prime * result + ((getId() == null) ? 0 : getId().hashCode());
    result = prime * result + ((getUsername() == null) ? 0 : getUsername().hashCode());
    result = prime * result + ((getNickName() == null) ? 0 : getNickName().hashCode());
    result = prime * result + ((getUserAccount() == null) ? 0 : getUserAccount().hashCode());
    result = prime * result + ((getUserPassword() == null) ? 0 : getUserPassword().hashCode());
    result = prime * result + ((getDirection() == null) ? 0 : getDirection().hashCode());
    result = prime * result + ((getIntroduction() == null) ? 0 : getIntroduction().hashCode());
    result = prime * result + ((getGender() == null) ? 0 : getGender().hashCode());
    result = prime * result + ((getAvatarUrl() == null) ? 0 : getAvatarUrl().hashCode());
    result = prime * result + ((getPhone() == null) ? 0 : getPhone().hashCode());
    result = prime * result + ((getEmail() == null) ? 0 : getEmail().hashCode());
    result = prime * result + ((getUserStatus() == null) ? 0 : getUserStatus().hashCode());
    result = prime * result + ((getCreateTime() == null) ? 0 : getCreateTime().hashCode());
    result = prime * result + ((getUpdateTime() == null) ? 0 : getUpdateTime().hashCode());
    result = prime * result + ((getIsDelete() == null) ? 0 : getIsDelete().hashCode());
    result = prime * result + ((getSalt() == null) ? 0 : getSalt().hashCode());
    result = prime * result + ((getRole() == null) ? 0 : getRole().hashCode());
    result = prime * result + ((getOpenId() == null) ? 0 : getOpenId().hashCode());
    result = prime * result + ((getCaptcha() == null) ? 0 : getCaptcha().hashCode());
    result = prime * result + ((getCaptchaTime() == null) ? 0 : getCaptchaTime().hashCode());
    return result;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append(getClass().getSimpleName());
    sb.append(" [");
    sb.append("Hash = ").append(hashCode());
    sb.append(", id=").append(id);
    sb.append(", username=").append(username);
    sb.append(", nickName=").append(nickName);
    sb.append(", userAccount=").append(userAccount);
    sb.append(", userPassword=").append(userPassword);
    sb.append(", direction=").append(direction);
    sb.append(", introduction=").append(introduction);
    sb.append(", gender=").append(gender);
    sb.append(", avatarUrl=").append(avatarUrl);
    sb.append(", phone=").append(phone);
    sb.append(", email=").append(email);
    sb.append(", userStatus=").append(userStatus);
    sb.append(", createTime=").append(createTime);
    sb.append(", updateTime=").append(updateTime);
    sb.append(", isDelete=").append(isDelete);
    sb.append(", salt=").append(salt);
    sb.append(", role=").append(role);
    sb.append(", openId=").append(openId);
    sb.append(", captcha=").append(captcha);
    sb.append(", captchaTime=").append(captchaTime);
    sb.append(", serialVersionUID=").append(serialVersionUID);
    sb.append("]");
    return sb.toString();
  }
}
