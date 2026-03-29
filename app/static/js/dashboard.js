const usersTitle = document.getElementById("usersTitle");
const usersCircle = document.getElementById("usersCircle");
const usersBar = document.getElementById("usersBar");
const usersPercent = document.getElementById("usersPercent"); 
const topUsers = document.getElementById("topUsers");
const topUsersPercent = document.getElementById("topUsersPercent");
const onlineUsers = document.getElementById("onlineUsers");
const onlineUsersPercent = document.getElementById("onlineUsersPercent");
const thisWeekUsers = document.getElementById("thisWeekUsers");
const thisWeekUsersPercent = document.getElementById("thisWeekUsersPercent");
const passiveUsers = document.getElementById("passiveUsers");
const passiveUsersPercent = document.getElementById("passiveUsersPercent");
const mainContent = document.getElementById("main-content");


let totalUsers=200;

let topUsersValue=80;
let onlineUsersValue=50;
let thisWeekUsersValue = 50;
let passiveUsersValue = 20;

let usersPercentValue=(totalUsers/totalUsers) * 100;
let topUsersPercentValue = (topUsersValue / totalUsers) * 100;
let onlineUsersPercentValue = (onlineUsersValue / totalUsers) * 100;
let thisWeekUsersPercentValue = (thisWeekUsersValue / totalUsers) * 100;
let passiveUsersPercentValue = (passiveUsersValue / totalUsers) * 100;



let fillTopUsers = 0;
let fillOnlineUsers=0;
let fillJoinedusers = 0;
let fillpassiveUsers = 0;
let fillUsersBar = 0;
let radius = 60;
let circumference = 2 * Math.PI * radius;

usersBar.style.strokeDasharray=circumference;
usersBar.style.strokeDashoffset=circumference;




let interval = setInterval(()=>{

    if(fillTopUsers <= topUsersPercentValue){
        topUsersPercent.style.background = `conic-gradient(green 0% ${fillTopUsers}%, rgba(255, 255, 255, 0) ${fillTopUsers}%  100%)`;
        topUsersPercent.innerHTML = `${fillTopUsers}<nav>%</nav>`;
        fillTopUsers++;
    }

    if(fillOnlineUsers <= onlineUsersPercentValue){
        onlineUsersPercent.style.background = `conic-gradient(orange 0% ${fillOnlineUsers}%, rgba(255, 255, 255, 0) ${fillOnlineUsers}%  100%)`;
        onlineUsersPercent.innerHTML = `${fillOnlineUsers}<nav>%</nav>`;
        fillOnlineUsers++;

    }

    if(fillJoinedusers <= thisWeekUsersPercentValue){
        thisWeekUsersPercent.style.background = `conic-gradient(green 0% ${fillJoinedusers}%, rgba(255, 255, 255, 0) ${fillJoinedusers}%  100%)`;
        thisWeekUsersPercent.innerHTML = `${fillJoinedusers}<nav>%</nav>`;
        fillJoinedusers++;
        

    }

    if(fillpassiveUsers <= passiveUsersPercentValue){

        passiveUsersPercent.style.background = `conic-gradient(red 0% ${fillpassiveUsers}%, rgba(255, 255, 255, 0) ${fillpassiveUsers}%  100%)`;
        passiveUsersPercent.innerHTML = `${fillpassiveUsers}<nav>%</nav>`;
        fillpassiveUsers++;

    }

}, 20);

let progressInterval = null;
let dataProgress = null;



function setUserProgress(percentProgress) {
    fillUserProgress = 0;

    if (progressInterval) {
        clearInterval(progressInterval);
    }

    progressInterval = setInterval(() => {
        if (fillUserProgress <= percentProgress) {
            offset = circumference * (1 - fillUserProgress / 100);
            usersBar.style.strokeDashoffset = offset;
            usersPercent.innerHTML = `${fillUserProgress}<nav>%</nav>`;
            fillUserProgress++;

        }
        else {
            clearInterval(progressInterval);
        }
    }, 10)

}
setUserProgress(usersPercentValue);


topUsers.addEventListener('click', ()=>{
    usersTitle.textContent=`Top Users`;
    usersBar.style.stroke='green';
    
    setUserProgress(topUsersPercentValue);
    fill = 0;
    if (dataProgress) {
        clearInterval(dataProgress);
    }
    dataProgress = setInterval(() => {
        if (fill <= topUsersPercentValue) {
            topUsersPercent.style.background = `conic-gradient(green 0% ${fill}%, rgba(255, 255, 255, 0) ${fill}%  100%)`;
            topUsersPercent.innerHTML = `${fill}<nav>%</nav>`;
            fill++;
        }

    }, 30);
    
    

});

onlineUsers.addEventListener('click', () => {
    usersTitle.textContent = `Online Users`;
    usersBar.style.stroke = 'orange';
    setUserProgress(onlineUsersPercentValue);

    fill = 0;
    if(dataProgress){
        clearInterval(dataProgress);
    }

    dataProgress = setInterval(() => {
        if (fill <= onlineUsersPercentValue) {
            onlineUsersPercent.style.background = `conic-gradient(orange 0% ${fill}%, rgba(255, 255, 255, 0) ${fill}%  100%)`;
            onlineUsersPercent.innerHTML = `${fill}<nav>%</nav>`;
            fill++;
        }

    }, 30);
});

thisWeekUsers.addEventListener('click', () => {
    usersTitle.textContent = `This week Users`;
    usersBar.style.stroke = 'green';
    setUserProgress(thisWeekUsersPercentValue);
    fill=0;
    if (dataProgress) {
        clearInterval(dataProgress);
    }
    dataProgress = setInterval(() => {
        if (fill <= thisWeekUsersPercentValue) {
            thisWeekUsersPercent.style.background = `conic-gradient(green 0% ${fill}%, rgba(255, 255, 255, 0) ${fill}%  100%)`;
            thisWeekUsersPercent.innerHTML = `${fill}<nav>%</nav>`;
            fill++;
        }

    }, 30);
});

passiveUsers.addEventListener('click', () => {
    usersTitle.textContent = `Passive Users`;
    usersBar.style.stroke = 'red';
    setUserProgress(passiveUsersPercentValue);

    fill=0;

    if (dataProgress) {
        clearInterval(dataProgress);
    }
    dataProgress = setInterval(() => {
        if (fill <= passiveUsersPercentValue) {
            passiveUsersPercent.style.background = `conic-gradient(red 0% ${fill}%, rgba(255, 255, 255, 0) ${fill}%  100%)`;
            passiveUsersPercent.innerHTML = `${fill}<nav>%</nav>`;
            fill++;
        }

    }, 30);
});

usersCircle.addEventListener('click', ()=>{
    usersTitle.textContent='Users';
    usersBar.style.stroke = 'rgb(128, 20, 90)';
    setUserProgress(usersPercentValue);
});






