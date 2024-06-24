var frm = $('#contactForm');
(function($){
    "use strict";
    frm.validator().on("submit",function(event){
        if(event.isDefaultPrevented())
        {
            formError();
            submitMSG(false,"آیا فرم خالی میخواهید بفرستید !؟");
        }
            else{
                event.preventDefault();
                submitForm();
            }
        });
            function submitForm(){
                $.ajax({
                    type:frm.attr('method'),
                    url:frm.attr('action'),
                    data:frm.serialize(),
                    success:function(){
                        $("#SubmitContact").toggle();
                        frm[0].reset();
                        $(".posts").prepend('<div class="col-md-6">'+
                        '<div class="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">' +
                            '<div class="col p-4 d-flex flex-column position-static">' +
                                '<h3 class="mb-0 text-success">با تشکر از ثبت پیام تان</h3>' +
                                '<p class="mb-auto">بزودی با شما تماس خواهیم گرفت</p>' +
                            '</div>' +
                        '</div>' +
                    '</div>' 
                    )
                    },
                    error : function(err) {
                        formError();
                        submitMSG(false,err);
                }
                });}
function formError(){
    frm.removeClass().addClass('shake animated').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend',
    function(){$(this).removeClass();}
    );}
function submitMSG(valid,msg){
    if(valid){var msgClasses="h4 text-left tada animated text-success";
}
else{
    var msgClasses="h4 mt-3 text-left text-danger";
}
$("#msgSubmit").removeClass().addClass(msgClasses).text(msg);}}(jQuery));