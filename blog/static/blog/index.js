if(window.attachEvent) {
    window.attachEvent('onload', main);
} else {
    if(window.onload) {
        var curronload = window.onload;
        var newonload = function(evt) {
            curronload(evt);
            main(evt);
        };
        window.onload = newonload;
    } else {
        window.onload = main;
    }
}

function main() {
    for (let element of document.querySelectorAll('.mdc-button')) {
        mdc.ripple.MDCRipple.attachTo(element);
    }
}