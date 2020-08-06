


        String.prototype.format = function(){
            var args = arguments;
            return this.replace(/\{(\d+)\}/gm, function(ms, p1){return typeof(args[p1]) == 'undefined' ? ms : args[p1]});
        }



        var g_nearby_array01=new Array();
        var g_nearby_array02=new Array();
        var g_keyword01;
        var g_keyword02;
        var g_process_value=0;
        var g_counter_sentence_re=0;

        function find_color(str,color,keyword){

            var strArr4= new Array();
            strArr4 = str.split(keyword);
            var retSTR="";
            for(var i=0;i<strArr4.length-1;i++){
                retSTR=strArr4[i];
                retSTR=retSTR+"<div  class=\"{0}\">{1}</div>".format(color,keyword);
            }
            retSTR=retSTR+strArr4[strArr4.length-1];
            return retSTR;
        }

        function format_span(strCenten){
            var flag01=0;
            var flag02=0;
            var retStr="";
            for(var i=0;i<g_nearby_array01.length;i++){
                if(strCenten.indexOf(g_nearby_array01[i])!=-1){
                    flag01=1;
                    break;
                }
            }

            for(var i=0;i<g_nearby_array02.length;i++){
                if(strCenten.indexOf(g_nearby_array02[i])!=-1){
                    flag02=1;
                    break;
                }
            }
            if(flag01==1&&flag02==1){               //增加底色
                retStr="<div  class=\"intro_yellow\">{0}</div>".format(strCenten);
                g_counter_sentence_re=g_counter_sentence_re+1;
            }
            else{
                retStr=strCenten;
            }
            //标记keyword01相关
            var retSTR01=retStr;
            for(var i=0;i<g_nearby_array01.length;i++){
                retSTR01=find_color(retSTR01,"intro_green",g_nearby_array01[i])
            }
            //标记keyword01
            var retSTR02=find_color(retSTR01,"intro_green_key",g_keyword01)
            //标记keyword02
            var retSTR03=retSTR02;
            for(var i=0;i<g_nearby_array02.length;i++){
                retSTR03=find_color(retSTR03,"intro_red",g_nearby_array02[i])
            }
            //标记keyword02相关
            var retSTR04=find_color(retSTR03,"intro_red_key",g_keyword02)
            return retSTR04;

        }
        //获取div下所有内容
        function get_div_context(){
            var retStr=""
            $("#context_area div").each(function(){         //所有的span标签
                retStr=retStr+$(this).text()
            });
            retStr=retStr+context_area.innerHTML;
            //retStr="成功，是一个动宾结构的汉语名词。同“胜利”。意思是指达到或实现某种价值尺度的事情或事件，从而获得预期结果叫做成功。出自《书·禹贡》：“禹锡玄圭，告厥成功。” 成功是指人或动物通过有意识努力，达到了预期目标。成功在动物世界里没有对错，一切都是为了竞争资源。而在人类社会成功还有另外一个衡量维度，即那些通过合法的且符合道德约束的行为到达预期目标的人被称为”成功的人“。人生会经历无数的成功和失败，希望我们失败时不要气馁，因为只要我们找到正确的方式且付出行动去实现，我们一定会到达预期目标，一定会成功！";
            return retStr;
        }

        function save_context(){
            var div_context=get_div_context();
			var params = {
			"title":document.getElementById('title').value,
			"context":div_context,
			};
            $.get("save_context", params,
              function(data){
                alert("Data Loaded: " + data);
                window.location.href="userPanel.html";
            });
        }

        function Check_keywords(){
            g_keyword01=document.getElementById('keyword01').value;
            g_keyword02=document.getElementById('keyword02').value;
<!--            g_keyword01="成功";-->
<!--            g_keyword02="达到";-->

			var params = {

			"keyword01":g_keyword01,
			"keyword02":g_keyword02,
			};

            g_process_value=0;//设置进度条
            var str="{0}%".format(g_process_value);
            process.style.width=str;
            process.innerHTML=str;


            $.get("get_nearby", params,
              function(data){
              var obj;
                try{
                     obj=JSON.parse(data);
                } catch(e) {
                   alert(data) ;
                   return;
                }

              g_nearby_array01=obj["Keyword01"];
              g_nearby_array02=obj["Keyword02"];
              console.log(g_nearby_array01)
              console.log(g_nearby_array02)

            var div_context=get_div_context();
            var centensArray= new Array();
            var strArr3 = div_context.split(".");
            for(var i=0;i<strArr3.length;i++){
                var strArr4= new Array();
                if(i<strArr3.length-1)
                    strArr4 = (strArr3[i]+".").split("。");
                else
                    strArr4 = (strArr3[i]).split("。");
                for(var j=0;j<strArr4.length;j++){
                    if(j<strArr4.length-1)
                        centensArray.push(strArr4[j]+"。");
                     else
                        centensArray.push(strArr4[j]);
                }
            }
            //var spanStr="<span style=\"color:blue\">abc</span> ";
            var spanStr="";

            for(var i=0;i<centensArray.length;i++){
               spanStr=spanStr+format_span(centensArray[i]);
            }
            console.log(spanStr);

            context_area.innerHTML=spanStr;
            //result show
            keyword1.innerHTML=g_keyword01;
            var mark_relate= g_counter_sentence_re/centensArray.length;
            if(mark_relate<0.3)
                strong.innerHTML="weak";
            else if(mark_relate<0.6)
                strong.innerHTML="moderate";
            else
                strong.innerHTML="strong";

            keyword2.innerHTML=g_keyword02;
            //出现
            keyword01_1.innerHTML=g_keyword01;

            keyword01_show.innerHTML="{0} time(s)".format((div_context.split(g_keyword01)).length-1)

            keyword02_01.innerHTML=g_keyword02;
            keyword02_show.innerHTML="{0} time(s)".format((div_context.split(g_keyword02)).length-1)
            //句子相关
            sentence_re.innerHTML="{0} sentence(s)".format(g_counter_sentence_re);
            g_counter_sentence_re=0;

            similiar.innerHTML=obj["similiar"];
            p1.innerHTML=obj["p1"];
            p2.innerHTML=obj["p2"];
            var school=obj["school"];
            console.log(school);
            });
        }

var int=self.setInterval("clock()",10);
function clock()
{
    if(g_process_value<100){
        g_process_value=g_process_value+10;
        var process=document.getElementById('process');
        var str="{0}%".format(g_process_value);
        process.style.width=str;
        process.innerHTML=str;
    }
}



