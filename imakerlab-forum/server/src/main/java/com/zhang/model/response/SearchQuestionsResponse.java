package com.zhang.model.response;

import com.zhang.base.response.PageResponse;
import com.zhang.model.entity.User;
import com.zhang.model.entity.Question;
import lombok.Data;

import java.util.List;

@Data
public class SearchQuestionsResponse extends PageResponse {
  private List<Question> questionList ;


  public SearchQuestionsResponse(long pageNo, long pageTotal, List<Question> questionList) {
    this.questionList = questionList;
    this.setPageNo(pageNo);
    this.setPageTotal(pageTotal);
  }

  public SearchQuestionsResponse(List<Question> questionList) {
    this.questionList = questionList;
  }

}
