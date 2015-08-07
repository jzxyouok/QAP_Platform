##数据服务接口
####1. login
用户登录

HTTP POST请求方式, 访问接口: http://127.0.0.1:10100/doUserAct/Login, 请求示例:

	curl -d "username=xxx&password=xxx" "http://127.0.0.1:10100/doUserAct"

请求参数格式说明:

	{
		"username": "flyfish",				// 登录用户名
		"password": "flyfish"				// 登录密码
	}

返回结果说明:
	
	{
		"code": 200,							// OK
		"data": {
			"username": "flyfish",			         // 用户名
			"access_token": "aej8emleui56ekwl",   // token串
			"ts": 1438874007					        // 时间戳（用于验证token是否过期）
	}

####2. register
用户注册

HTTP POST请求方式, 访问接口: http://127.0.0.1:10100/doUserAct/Register, 请求示例:

	curl -d "username=xxx&password=xxx&grade=xxx&user_type=xxx&serial_number=xxx&options={\"phone_number\": xxx, ...}" "http://127.0.0.1:10100/doUserAct/Register"

请求参数格式说明:

	{
		"username": "flyfish",				    // 注册用户名
		"password": "flyfish",			       // 注册密码
		"grade": 1,							   //  注册年级(0: 小学 1: 初中 2: 高中)
		"identifier": 0,				          // 用户身份类别 (0: 学生 1: 教师)
		"serial_number": 1103710520,		   // 教师工作证号(学生注册不填写)
		"options": {"phone_number": 15145102540, ....}    // 选填信息(Json序列串, 注意格式)
	}
	
返回结果说明:

	{
		"code": 200,							// OK, 其余状态码均失败
		"data": {
			"msg": "注册成功"
		}
	}

