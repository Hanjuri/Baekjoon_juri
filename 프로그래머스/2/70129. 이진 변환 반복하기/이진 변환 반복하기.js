function convert(s) {
    let sArr = s.split("");
    let firstArr = sArr.filter((each) => each === "1" );
    let zeroCount = sArr.length - firstArr.length;
    let secondTemp = firstArr.length;
    let ans = []
    while(secondTemp > 0){
        let temp = secondTemp % 2;
        ans.push(temp);
        secondTemp  = Math.floor(secondTemp / 2);

    }
    return [ans.reverse().join(""), zeroCount];
}

function solution(s){
    let temp = s;
    let step = 0;
    let zeroSum = 0;
    while(temp !== "1"){
        let [newTemp, zeroCount] = convert(temp);
        temp = newTemp;
        step++;
        zeroSum += zeroCount;
    }

    return [step, zeroSum];
}
