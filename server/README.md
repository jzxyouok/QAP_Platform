##数据服务接口
####1. login
登录

HTTP POST请求方式, 访问接口: http://127.0.0.1:10100/doUserAct, 请求示例:

	curl -d "username=xxx&password=xxx" "http://127.0.0.1:10100/doUserAct"

请求参数格式说明:

	{
		"username": "flyfish",				// 登录用户名
		"password": "flyfish"				// 登录密码
	}

返回结果说明:
	
	{
		"username": "flyfish",				// 用户名
	}