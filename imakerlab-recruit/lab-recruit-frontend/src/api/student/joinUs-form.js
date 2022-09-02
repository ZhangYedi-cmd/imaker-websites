import services from "../../untils/requests";

export const submitRegForm = (params) => services.post("/student/reg/", params);

