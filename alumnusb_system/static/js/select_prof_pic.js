var selected = null;

$(document).ready(function(){
    //Get every button
    var imgBtns = $('.prof-pic-btn');
    var succMsg = $('#success-alert');
    var infoMsg = $('#info-alert');
    var failMsg = $('#fail-alert');

    //Check if the user has a seleced img
    if(userImg!=-1){ //userImg defined in the html file
        imgBtns.each(function(){
            console.log($(this).data("imgid") + ", "+ userImg );
            if ( $(this).data("imgid")==userImg ){
                updateSelected($(this));
            }
        });
        
    }

    $('.prof-pic-btn').click(function(e){
        console.log(this.id);
        updateSelected($("#"+this.id));
    });

    $('#update-pic-form').submit(function(e){
        e.preventDefault();
        resetMsgs();
        if(selected==null){
            infoMsg.removeClass("d-none");
            return;
        }

        var form = $("#" + this.id);
        var selectedField = $('#selected-img');
        var dataUrl = form.data("url");

        selectedField.val(selected.data("imgid"));
        //Perform an ajax post request
        $.ajax({
            type:'POST',
            url: dataUrl,
            data:form.serialize(),

            success:function(json){
                succMsg.removeClass("d-none");
                console.log("Everything ok");
            },
            
            error:function(xhr, errmsg,err){
                failMsg.removeClass("d-none");
                console.log("Something went wrong");
            }
        });
        
    });


    //This functions updates the currently selected img
    function updateSelected(newItem){
        if(selected!=null){
            selected.removeClass("btn-warning");
            selected.addClass("btn-light");
        }
        newItem.addClass("btn-warning");
        newItem.removeClass("btn-light");
        selected = newItem;
    }

    function resetMsgs(){
        succMsg.addClass("d-none");
        failMsg.addClass("d-none");
        infoMsg.addClass("d-none");
    }
});