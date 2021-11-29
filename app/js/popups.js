function arbiterpopup1() {

    alert("You have entered the Arbiter Pool!")
   
    // await sleep(5);
  
    alert("Congrats! You have been selected as an arbiter. See the evidence below.")
    document.getElementById('btnHolder').innerHTML = '<input type="button" onClick="evidenceBtn();" value="Show Evidence" />';


}

function arbiterpopup2() {

    alert("Congrats! You have been selected as an arbiter.")
}

function evidenceBtn(){
  //document.getElementById('btnHolder').innerHTML = obj.innerHTML;
  document.getElementById("btnHolder").innerHTML = "https://bafybeiclpu3wxd2pjcr5e2ebltznddbxabvdog6hyigqnnpafegvmkjnlm.ipfs.dweb.link/" ;
}