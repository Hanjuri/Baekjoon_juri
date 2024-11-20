const fs = require("fs");
const input = fs.readFileSync(0).toString().trim();

// 변수 선언 및 입력
const [k, n] = input.split(" ").map(Number);

function printAnswer(arr){
    console.log(arr.join(' '));
}
function allElementsTree(arr){
    let count = 1;
    for(let i = 0; i < arr.length; i++){
        if(arr[i] === arr[i-1]){
            count++;
            if (count >= 3){
                return true;
            }
        }else{
            count = 1;
        }
    }
    return false;
}

function sol(cnt, ans){
    if(cnt === n){
        if(!allElementsTree(ans)){
                printAnswer(ans);
            }
        
        return;
    }
    for (let i = 1; i < k+1; i++) {
        ans.push(i);
        sol(cnt+1, ans);
        ans.pop();
    }
}
sol(0,[]);
