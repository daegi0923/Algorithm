function solution(n, times) {
    let left = 1
    let right = times[times.length-1]*n
    let answer = right
    
    while(left <=right){
        const mid = Math.floor((left + right)/2)
        
        const people = times.reduce((acc, cur)=>{
            return acc + Math.floor(mid/cur)
        }, 0)
        // console.log(left, mid,right, people)
        if(people < n){
            left = mid + 1
        }else{
            answer = mid
            right = mid - 1
        }
    }
    return answer
}