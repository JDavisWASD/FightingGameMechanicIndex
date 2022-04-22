function openMainTab(event, tabID) {
    var i, mainTabContent, mainTabLinks;
    mainTabContent = document.getElementsByClassName('mainTabContent');
    for (i = 0; i < mainTabContent.length; i++) {
        mainTabContent[i].style.display = 'none';
    }

    mainTabLinks = document.getElementsByClassName('mainTabLinks');
    for (i = 0; i < mainTabLinks.length; i++) {
        mainTabLinks[i].className = mainTabLinks[i].className.replace(' active', '');
    }
    
    document.getElementById(tabID).style.display = 'block';
    event.currentTarget.className += ' active';
}

function openSubTab(event, tabID) {
    var i, subTabContent, subTabLinks;
    subTabContent = document.getElementsByClassName('subTabContent');
    for (i = 0; i < subTabContent.length; i++) {
        subTabContent[i].style.display = 'none';
    }

    subTabLinks = document.getElementsByClassName('subTabLinks');
    for (i = 0; i < subTabLinks.length; i++) {
        subTabLinks[i].className = subTabLinks[i].className.replace(' active', '');
    }
    
    document.getElementById(tabID).style.display = 'block';
    event.currentTarget.className += ' active';
}

document.getElementsByClassName('gameOption').addEventListener('change', function() {
    
})