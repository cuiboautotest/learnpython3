#coding:utf-8
from untils.excel_tool import excel_tool
from untils.send_request import send_request
from untils.log_trace import *
from untils.check_result import CheckResult
import  json
headers = {
    "X-Token":"0a6db4e59c7fff2b2b94a297e2e5632e"
}

class runner():
    def __init__(self):
        self.excel = excel_tool("../testcase/test.xls")
        self.check = CheckResult()

    def join_case(self):
        global  skip_list,sucess_list,failed_list,skip_list
        sucess_list = []
        sucess_list = []
        failed_list = []
        skip_list = []

        for row in range(1,self.excel.rows):
            no = self.excel.get_caseno(row)
            url = self.excel.get_caseurl(row)
            isrun = self.excel.get_runflag(row)
            name = self.excel.get_casename(row)
            level = self.excel.get_caselevel(row)
            data = self.excel.get_casebody(row)
            expect_res = self.excel.get_expectres(row)
            method = self.excel.get_methodtype(row)
            hasheader = self.excel.get_headerflag(row)
            operator = self.excel.get_operator(row)

            if isrun == "Y":
                logging.info("Begin to run test case : %s,case number :%s" %(name,no))
                logging.info("Request method type is :%s" %method)
                logging.info("Request URL:%s" %url)
                logging.info("Request Body:%s" %json.dumps(json.loads(data),sort_keys=True,indent=2))
                res = send_request(method,url,data=data,headers=headers)


                is_sucess = self.check.cmpdict(eval(expect_res),eval(res.text),operator)
                print(is_sucess)
                if is_sucess:
                    sucess_list.append(name)
                    #回写测试结果
                    self.excel.write_testres(row,"pass")
                    #回写实际结果
                    self.excel.write_actualres(row,res.text)
                    logging.info("Test case %s run sucess." %name)
                else:
                    failed_list.append(name)
                    print("fail",is_sucess)
                    #回写测试结果
                    self.excel.write_testres(row,"failed")
                    #回写实际结果
                    self.excel.write_actualres(row,res.text)
                    logging.error("Test case %s run fail." %name)

                logging.info("Response is:%s" %json.dumps(res.json(),sort_keys=True,indent=2))

            else:
                skip_list.append(name)
                self.excel.write_testres(row,"skipped")

    def sum(self):

        total = len(sucess_list)+len(failed_list) + len(skip_list)
        failed = len(failed_list)
        sucess = len(sucess_list)

        logging.info("-----------------------------------------------------------")
        logging.info("本次一共运行：%s 个用例" %total)
        logging.info("本次运行通过：%s 个用例" %sucess)
        logging.info("本次运行跳过：%s 个用例" %len(skip_list))
        logging.info("跳过的用例：%s" %skip_list)
        logging.info("-----------------------------------------------------------")