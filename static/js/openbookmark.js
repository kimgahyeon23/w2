// form
let frm = document.forms["frm"];
// 버튼들
let addBtn = document.getElementById("submit-btn");
let resetBtn = document.getElementById("reset-btn");
// 북마크 리스트
let bookmarkList = document.getElementById("bookmark-list");
// form reset
function reset() {
 frm.elements.namedItem("id").value = ''
 frm.elements.namedItem("title").value = '';
 frm.elements.namedItem("url").value = '';
}
// 취소 버튼 핸들러 등록
resetBtn.addEventListener("click", reset);

//DOM에 새로운 bookmark 정보 추가
function addItem(bookmark){
    let templ = `
    <a href="${bookmark.url}" class="bookmark-link">${bookmark.title}</a>
    [<a href="#" class="edit-btn">수정</a>]
    [<a href="#" class="delete-btn">삭제</a>]
    `;
    let el = document.createElement('li');
    el.dataset.itemId = bookmark.id;
    //dataset 을 이용하면 css 사용자가 만든 속성이 됌
    //css를 통하면 data-item-id = "id값" 이 됌
    //이를 하는이유는 나중에 이 데이터를 삭제하려할때 id값으로 빠르게
    //찾기 위함
    el.classList.add("list-item");
    el.innerHTML = templ;
    bookmarkList.appendChild(el);
}
//초기 목록 얻기
axios.get("http://127.0.0.1:8000/api/bookmark")
.then(res=>{
    console.log(res);
    res.data.datas.forEach(item=>addItem(item));
}).catch(e=>console.log(e));

//bookmark 삭제
bookmarkList.onabort("click", ".delete-btn", function(e){
    if(!confirm("삭제하시겠습니까?")) return;

    let el = this.closest(".list-item");
    let itemId = el.dataset.itemId;

    axios.delete(`http://127.0.0.1:8000/api/bookmark/${itemId}`)
    .then(res=>el.remove())
    .catch(e=>console.log(e));
})


// 사용 용도 댓글삭제 아이디 중복체크 좋아요 싫어요 등