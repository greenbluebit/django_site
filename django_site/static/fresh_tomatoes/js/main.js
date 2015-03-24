


$(document).ready(function() {

    $('#search').on('click', function() {
        window.open('/fresh_tomatoes/search/' + $('header input').val(), '_self' );
    });

    $('header input').keypress(function(ev) {
        if( ev.which == 13) {
            ev.preventDefault();
            window.open('/fresh_tomatoes/search/' + $('header input').val(), '_self' );
        }
    });

    var asyncLoop = function(o){
            var i=-1,
                length = o.length;

            var loop = function(){
                i++;
                if(i==length){i = 0;loop(); return;}
                o.functionToLoop(loop, i);
            }
            loop();//init
        }
    setTimeout(function() {

        asyncLoop({
            length : 6,
            functionToLoop : function(loop, i){
                setTimeout(function(){
                    $('#favicon').remove();
                    $('head').append('<link href="/static/fresh_tomatoes/images/favicon ('+i+').ico" id="favicon" rel="shortcut icon">');
                    loop();
                },700);
            },
            callback : function(){
            }
        });
    },200);


    $('header button').on('click', function() {
        console.log(this.className);
        if($('.'+this.className).hasClass('movie-btn')) {
            console.log('movie');
            $('.'+this.className).addClass('active');
            $('.show-btn').removeClass('active');
            $('#movies').css('display', 'block');
            $('#shows').css('display','none');
        } else {
            console.log('show');
            $('.'+this.className).addClass('active');
            $('.movie-btn').removeClass('active');
            $('#shows').css('display', 'block');
            $('#movies').css('display','none');
        }
    });
    $('.art').on('click', articleShow);
    $('.zoomed').on('click', function() {
        $('.zoomed').css('opacity', '0');
        $('.zoomed').css('pointer-events', 'none');
        $('#full-art').html('');
    })

});

function articleShow() {
    var element = this;
    var children = this.children;
    var extra = children[2];
    console.log();
    var zoomed = $('.zoomed');
    $('#full-art').html(extra.innerHTML);
    window.scrollTo(0, 0);
    zoomed.css('opacity','1');
    zoomed.css('pointer-events', 'all');
}