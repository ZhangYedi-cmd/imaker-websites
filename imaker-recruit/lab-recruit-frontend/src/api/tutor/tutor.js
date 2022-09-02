import services from "../../untils/requests";

export const login = (params) => services.post("/tutor/login", params);

export const register = (params) => services.post('/tutor/register', params);

// 后端会返回用户的uid 和 username
// 整合Vuex使用
export const get_base_info = (params) => services.get('/tutor/getBaseInfo');

export const getStudentList = (params) => services.get('/student/list', {params: params});

// 虽然接口是修改状态,但是学生的所有信息都可以修改的
export const changeStudentInfo = (params) => services.post('/student/changeStatus', params);

export const getStudentSummary = (params) => services.get('/student/summary', {params: params});

// 删除学生
export const deleteStudent = (params) => services.post('/student/delete', params);

// 更改注释
export const addAnnotation = (params) => services.post('/student/annotation', params);

/**
 * leader 获取导师列表
 * */
export const getTutorList = (params) => {
  return services.get('/tutor/list', {params: params});
}

/**
 * 删除导师
 * */
export const deleteTutor = (params) => services.post('/tutor/delete', params);
