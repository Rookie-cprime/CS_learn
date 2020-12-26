(* Dan Grossman, Coursera PL, HW2 Provided Code *)

(* if you use this function to compare two strings (returns true if the same
   string), then you avoid several of the functions in problem 1 having
   polymorphic types that may be confusing *)
fun same_string(s1 : string, s2 : string) =
    s1 = s2
fun list_append pattern=
    case pattern of
	([],l2) => l2
	| (x::xs',l4) => x::list_append(xs',l4)    

(* put your solutions for problem 1 here *)

fun all_except_option pattern=
    case pattern of
	(_,[]) => NONE
	       | (a,x::xs') => if same_string(a,x) then SOME xs'
			       else
				   let
				       val c = all_except_option(a,xs')
				   in
				       case c of
					   NONE => NONE
					   | SOME l => SOME (x::l) 
				   end

fun get_substitutions1 pattern =
    case pattern of
	([],_) => []
	|(x::xs',s1)  => let val a = all_except_option (s1,x) in
			     case a of
				 NONE => get_substitutions1 (xs',s1)
			|SOME l => list_append(l,get_substitutions1 (xs',s1))
								    end

fun get_substitutions2 (ls,s1) =
    let 
	fun hp1 pattern =
	    case pattern of
		([],_,sl1)=>sl1
		|(x::xs',s,sl2) => let val a = all_except_option (s,x) in
				       case a of
					   NONE => hp1(xs',s ,sl2)
					|SOME l  =>hp1(xs',s,list_append(sl2,l))
						      end
    in
	hp1(ls,s1,[])
    end


fun similar_names (ls,dic)=
    let
	val l1 = get_substitutions2(ls,#first dic)
	fun gener pattern =
	    case pattern of
		[] => []
	|x::xs'  => {first = x,last = #last dic,middle = #middle dic}::gener(xs')
   in
       dic::gener(l1)
   end

(* you may assume that Num is always used with values 2, 3, ..., 10
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades
datatype rank = Jack | Queen | King | Ace | Num of int 
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw 

exception IllegalMove

(* put your solutions for problem 2 here *)
