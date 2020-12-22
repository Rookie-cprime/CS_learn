fun is_older(d1:int*int*int,d2:int*int*int)=
    if #1 d1 < #1 d2
    then true
    else if #1 d1 = #1 d2 andalso #2 d1 < #2 d2
    then true
    else if #1 d1 = #1 d2 andalso #2 d1 = #2 d2 andalso #3 d1 < #3 d2
    then true
    else false

fun number_in_month(l:(int*int*int) list,month:int)=
    if null l
    then 0
    else if #2 (hd l)= month
    then 1 + number_in_month(tl l,month)
    else number_in_month(tl l,month)

fun number_in_months(l:(int*int*int) list,months:int list)=
    if null months
    then 0
    else number_in_month(l,hd months)+number_in_months(l,tl months)

fun append(xs,ys)=
    if null xs
    then ys
    else (hd xs)::append((tl xs),ys)

fun dates_in_month(dates:(int*int*int) list,month:int)=
    let
	val new_dates = []
    in
	if null dates
	then   new_dates
	else if #2 (hd dates)=month
	then   (hd dates)::dates_in_month((tl dates),month)
        else dates_in_month((tl dates),month)
    end

fun dates_in_months(dates:(int*int*int) list,months:int list)=
    let
	val new_dates = []
    in
	if null months
	then new_dates
	else append(dates_in_month(dates,(hd months)),dates_in_months(dates,(tl months)))
    end

fun get_nth(l,nth:int)=
    if nth = 1
    then (hd l)
    else get_nth((tl l),nth-1)

fun date_to_string(dates:int*int*int)=
let
    val month_l = ["January","February","March","April","May","June","July","August", "September","October","November","December"]
in
    get_nth(month_l,#2 dates)^" "^Int.toString(#3 dates)^", "^Int.toString(#1 dates)
end

fun number_before_reaching_sum(sum:int,num_list:int list)=
    let
    fun sum_list(x0:int,x1:int,x2:int list)=
	if x0 >= sum
        then x1
        else sum_list(x0+(hd (tl x2)),(hd x2),tl x2)
    in
       sum_list(hd num_list,0,num_list)
    end

fun what_month(day:int)=
    let
	val l = [31,28,31,30,31,30,31,31,30,31,30,31]
        fun sum_list(x0:int,x1:int,x2:int list)=
	    if x0 >= day
	    then x1
            else sum_list(x0+(hd (tl x2)),x1+1,tl x2)
    in
	sum_list(hd l,1,l)
    end

fun month_range(from:int,to:int)=
    let
	fun count_down(x1:int,x2:int list)=
	    if x1<from
	    then x2
            else count_down(x1-1,what_month(x1)::x2)
    in
	count_down(to,[])
    end

fun oldest(dates:(int*int*int) list)=
    let
       fun older(datess:(int*int*int) list,date:(int*int*int))=
	   if null datess
	   then date
           else if is_older(date,hd datess)
           then older(tl datess,date)
           else older(tl datess,hd datess)
    in
	SOME(older(tl dates,hd dates))
    end
