import services from "../../untils/requests";

export const getGroupList = (params) => {
  return services.get('/group/list');
}

export const deleteGroup = (params) => services.post('/group/delete',params);

export const newGroup = (params) => services.post('/group/newGroup', params);
