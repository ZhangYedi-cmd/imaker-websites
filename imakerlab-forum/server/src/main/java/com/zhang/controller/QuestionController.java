package com.zhang.controller;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.zhang.base.request.DelParams;
import com.zhang.base.response.BaseResponse;
import com.zhang.base.response.ResultUtils;
import com.zhang.exception.BusinessException;
import com.zhang.model.entity.Question;
import com.zhang.model.entity.User;
import com.zhang.model.enums.ErrorCodeEnum;
import com.zhang.model.request.SearchQuestionRequest;
import com.zhang.model.response.SearchQuestionsResponse;
import com.zhang.service.QuestionService;
import org.apache.commons.lang3.StringUtils;
import org.apache.logging.log4j.util.Strings;
import org.apache.tomcat.util.http.ResponseUtil;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;

@RestController
@RequestMapping("/api/question")
public class QuestionController {
  @Resource
  private QuestionService questionService;

  @GetMapping("/search")
  public BaseResponse<IPage<Question>> searchQuestions(SearchQuestionRequest request) {
    if (request == null) {
      throw new BusinessException(ErrorCodeEnum.REQUEST_PARAMS_ERROR);
    }
    QueryWrapper<Question> queryWrapper = new QueryWrapper<>();
    queryWrapper.like("title", request.getTitle());
    IPage<Question> userPage = questionService.page(new Page<>(request.getPageNo(), request.getPageSize()), queryWrapper);
    return ResultUtils.success(userPage);
  }

  @PostMapping("/delete")
  public BaseResponse<Boolean> delQuestion(@RequestBody DelParams delParams) {
    if (delParams == null) {
      throw new BusinessException(ErrorCodeEnum.REQUEST_PARAMS_ERROR);
    }
    Long questionId = delParams.getId();
    if (questionId < 0) {
      throw new BusinessException(ErrorCodeEnum.REQUEST_PARAMS_ERROR);
    }
    questionService.removeById(delParams.getId());
    return ResultUtils.success(null, "删除成功");
  }

  @PostMapping("/update")
  public BaseResponse<Question> updateQuestion(@RequestBody Question question) {
    if (question == null) {
      throw new BusinessException(ErrorCodeEnum.REQUEST_PARAMS_ERROR);
    }
    Long questionId = question.getQuestionId();
    if (questionId < 0) {
      throw new BusinessException(ErrorCodeEnum.REQUEST_PARAMS_ERROR);
    }
    questionService.updateById(question);
    return ResultUtils.success(question, "更新成功！");
  }

//  @PostMapping("/add")
//  public BaseResponse<Boolean> addQuestion(@RequestBody Question question) {
//    if (question == null) {
//      throw new BusinessException(ErrorCodeEnum.REQUEST_PARAMS_ERROR);
//    }
//    if (StringUtils.isAnyBlank())
//  }
}
