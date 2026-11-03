const {chromium}=require('playwright');
const out='F:/Github Repos/projects/levelup-crm/proof/ui/';
(async()=>{
const b=await chromium.launch();const c=await b.newContext({viewport:{width:1440,height:860}});const p=await c.newPage();
const errs=[];p.on('console',m=>{if(m.type()==='error')/WebSocket|ERR_CONNECTION/.test(m.text())||errs.push(m.text())});p.on('pageerror',e=>errs.push(String(e)));
await p.goto('http://localhost:5211/');
await p.evaluate(()=>{localStorage.clear();localStorage.setItem('teamlog_current_user_id','user-admin');
localStorage.setItem('teamlog_projects',JSON.stringify([{id:'proj-1',name:'Cyberpunk VFX Sequence',code:'C',color:'#000',deadlineDate:'2026-11-02',leadAssigneeId:'',leadAssigneeName:'',isActive:true}]));
localStorage.setItem('teamlog_tasks',JSON.stringify([{id:'task-101',title:'Houdini smoke',project:'Houdini Fluid Simulation',assignedToId:'user-haroon',assignedToName:'Haroon Malik',status:'Working',priority:'High',assignedDate:'2026-11-04',deadlineDate:'2026-11-05',deadlineTime:'05:00 PM',estimatedMinutes:60,timeTakenMinutes:0,progress:0,notes:'',description:'',createdById:'user-admin',updatedAt:new Date().toISOString()}]));});
await p.reload();
const bad=/Cyberpunk|Houdini|Automotive|Clean Plate|ShotGrid|NAS\b|AWS|Nuke|NaN|Infinity/;
let fail=0;
for(const [path,shot] of [['/home','clean-home'],['/tasks','clean-empty'],['/tasks?v=board','clean-board'],['/tasks?v=calendar',null],['/projects',null],['/docs',null],['/timesheet',null],['/dashboards',null],['/reports',null],['/performance',null],['/progress',null]]){
 await p.goto('http://localhost:5211'+path);await p.waitForTimeout(700);
 const t=await p.evaluate(()=>document.body.innerText);const m=t.match(bad);
 console.log((m?'FAIL':'PASS'),path,m?m[0]:'',t.length<80?'(short text)':'');if(m)fail++;
 if(shot)await p.screenshot({path:out+shot+'.png'});
 await p.screenshot({path:'C:/Users/KHIZAR~1/AppData/Local/Temp/s_'+path.replace(/\W/g,'_')+'.png'});
}
const ls=await p.evaluate(()=>[localStorage.getItem('teamlog_data_version'),localStorage.getItem('teamlog_tasks')]);
console.log(ls[0]==='2'&&ls[1]==='[]'?'PASS':'FAIL','cleanup',ls);
console.log(errs.length?'FAIL':'PASS','console errors',errs.slice(0,5));
await b.close();})();
