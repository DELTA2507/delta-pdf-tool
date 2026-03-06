function showTab(id){

document.querySelectorAll(".tab").forEach(t=>{
t.classList.remove("active")
})

document.querySelectorAll(".navbtn").forEach(b=>{
b.classList.remove("active")
})

document.getElementById(id).classList.add("active")

event.target.classList.add("active")

}



async function compress(){

const file=document.getElementById("compressFile").files[0]

if(!file){
alert("Select a PDF")
return
}

const output=file.path.replace(".pdf","_compressed.pdf")

await window.pywebview.api.compress(file.path,output)

document.getElementById("compressStatus").innerText="Compression completed"

}



async function merge(){

const files=[...document.getElementById("mergeFiles").files]

if(files.length<2){
alert("Select at least 2 PDFs")
return
}

const paths=files.map(f=>f.path)

await window.pywebview.api.merge(paths,"merged.pdf")

document.getElementById("mergeStatus").innerText="Merge completed"

}



async function compressFolder(){

const files=[...document.getElementById("folderSelect").files]

if(files.length===0){
alert("Select a folder")
return
}

const folder=files[0].path.split("\\").slice(0,-1).join("\\")

await window.pywebview.api.compress_folder(folder)

document.getElementById("folderStatus").innerText="Folder compression completed"

}