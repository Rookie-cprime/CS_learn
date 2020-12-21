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
