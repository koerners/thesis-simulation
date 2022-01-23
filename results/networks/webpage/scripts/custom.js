$(document).ready(function() {
    // Custom Cytoscape.JS code goes here.

    // Example: add linkouts to nodes that opens the "href" node attribute on click
    // cy.on('tap', 'node', function(){
    //   try { // your browser may block popups
    //     window.open( this.data('href') );
    //   } catch(e){ // fall back on url change
    //     window.location.href = this.data('href');
    //   }
    // });

    // For more options, check out http://js.cytoscape.org/

    function sortOptions() {
        var options = document.getElementById('network-selector').options;
        var optionsArray = [];
        for (var i = 0; i < options.length; i++) {
            optionsArray.push(options[i]);
        }
        optionsArray = optionsArray.sort(function(a, b) {
            return a.innerHTML.toLowerCase().charCodeAt(0) - b.innerHTML.toLowerCase().charCodeAt(0);
        });

        for (var i = 0; i <= options.length; i++) {
            options[i] = optionsArray[i];
        }
        options[0].selected = true;
    }

    sortOptions();
});