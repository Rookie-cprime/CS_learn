fun map(f,xs) =
    case xs of
	[] => []
     | x::xs' => (f x)::map(f,xs')

val x1 = map((fn x => x+1),[4,8,12,16])
val x2 = map(hd,[[1,2],[3,4],[5,6,7]])

fun filter(f,xs) =
    case xs of
	[] => []
     | x::xs' => if f x
		      then x::(filter (f,xs'))
		      else filter(f,xs')

fun all_even xs = filter((fn v => (v mod 2 = 0)),xs)
