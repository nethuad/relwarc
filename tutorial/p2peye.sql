drop table p2peye_platform_detail;
create table p2peye_platform_detail as 
select pname
,trim(leading '/' from href) as href
,tags 
,descriptions
,substring(tags from '(天眼评级上榜)，最新排名：第[\d]+名（全部[\d]+家）') as isboard
,cast(substring(tags from '天眼评级上榜，最新排名：第([\d]+)名（全部[\d]+家）') as bigint) as board_order
,cast(substring(tags from '天眼评级上榜，最新排名：第[\d]+名（全部([\d]+)家）') as bigint) as board_total
,cast(substring(tags from '最新数据排名：第([\d]+)名（全部[\d]+家）') as bigint) as data_order
,cast(substring(tags from '最新数据排名：第[\d]+名（全部([\d]+)家）') as bigint) as data_total
,substring(tags from '家）。,(.*)}') as tag_array
,substring(descriptions from '预期利率：([\d\.\~%]+%),') as profit_rate
,substring(descriptions from '运营状态：([^,]+),') as status
,substring(descriptions from '注册资本：([\d]+万),') as register_capital
,substring(descriptions from '注册地：([^,]+),') as register_address
,substring(descriptions from '用户评价：(\[.*\])') as comment_tag
,substring(descriptions from '(\d+%)好评度') as comment_goodrate
,substring(descriptions from '(\d+)人点评') as comment_nums
from p2peye_platform 
;


select pname
,href
,isboard
,board_order
,board_total
,data_order
,data_total
,tag_array
,profit_rate
,status
,register_capital
,register_address
,comment_tag
,comment_goodrate
,comment_nums
-- select * 
from p2peye_platform_detail
order by board_order,data_order
;

where pname in ('雪山贷','团贷网','信诺金融','团贷网','陆金服','宜人贷','拍拍贷')
;
