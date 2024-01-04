fun search(list, first, last, target)
    $print(first)
    $print(last)
    if first <= last then
        let mid = int((first+last)/2)
        if target == (list/mid) then
            return mid
        elif target < (list/mid) then
            return search(list, first, mid-1, target)
        else
            return search(list, mid+1, last, target)
        end
    end
    return -1
end


let a = [1,2,2,3]

let v = 1

let val = search(a, 0, len(a)-1, v)

if val == -1 then
    print("5 not found")
else
    print("5 found")
end