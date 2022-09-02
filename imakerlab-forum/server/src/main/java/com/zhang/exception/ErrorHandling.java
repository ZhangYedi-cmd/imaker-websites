package com.zhang.exception;

import com.alibaba.druid.wall.violation.ErrorCode;
import com.zhang.base.response.BaseResponse;
import com.zhang.base.response.ResultUtils;
import com.zhang.model.enums.ErrorCodeEnum;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.converter.HttpMessageNotReadableException;
import org.springframework.web.bind.MissingServletRequestParameterException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@Slf4j
@RestControllerAdvice
public class ErrorHandling {

  /**
   * 全局处理异常
   *
   * @param e
   */
  @ResponseStatus(HttpStatus.BAD_REQUEST)
  @ExceptionHandler({BusinessException.class})
  public BaseResponse<String> handlePowerException(BusinessException e) {
    log.error(e.getCode() + e.getMessage());
    return ResultUtils.error(e.getCode(), e.getMessage());
  }

//  /**
//   * 400 - Bad Request
//   */
//  @ResponseStatus(HttpStatus.BAD_REQUEST)
//  @ExceptionHandler(HttpMessageNotReadableException.class)
//  public BaseResponse<String> handleHttpMessageNotReadableExceptionException(HttpMessageNotReadableException e) {
//    log.error("缺少请求参数", e);
//    return ResultUtils.error(ErrorCodeEnum.NULL_PARAMS.getCode(),e.getMessage());
//  }

//    @ExceptionHandler(BusinessException.class)
//    public BaseResponse<String> handlePowerException(BusinessException e) {
//        log.error(e.getCode() + e.getMessage());
//        return ResultUtils.error(e.getCode(), e.getMessage());
//    }

}
