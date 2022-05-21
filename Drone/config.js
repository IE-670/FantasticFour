// This .js file is auto-generated by `createCesium()` from VeRoViz
// The configs for cesium application go to here

function setConfigs() {
    viewer.camera.flyTo({
        destination: Cesium.Rectangle.fromDegrees(-78.806270, 42.984356, -78.767730, 43.014067) 
    });
    viewer.clock.currentTime = Cesium.JulianDate.addSeconds('2022-05-20T07:29:45Z', 0, new Cesium.JulianDate());
    allIDs = [
        'o-Drone-/veroviz/models/drone.gltf-stationary', 
        'o-Drone-/veroviz/models/drone.gltf-vertical', 
        'o-Drone-/veroviz/models/drone.gltf-move', 
        'o-wedge_1-/veroviz/models/wedge_black.gltf-move', 
        'o-wedge_2-/veroviz/models/wedge_white.gltf-move'    
    ];
    orientationIDs = [
        'o-Drone-/veroviz/models/drone.gltf-move', 
        'o-wedge_1-/veroviz/models/wedge_black.gltf-move', 
        'o-wedge_2-/veroviz/models/wedge_white.gltf-move'    
    ];
    czmlRouteFile = '/Drone/routes.czml';
    runRoutes(czmlRouteFile, allIDs, orientationIDs);
objectInfo['Drone-/veroviz/models/drone.gltf'] = {
    label : 'Drone (/veroviz/models/drone.gltf)', 
    childModels : ['o-Drone-/veroviz/models/drone.gltf-stationary', 'o-Drone-/veroviz/models/drone.gltf-vertical', 'o-Drone-/veroviz/models/drone.gltf-move'],
    scale : 100, 
    minPxSize : 75 
}; 
objectInfo['wedge_1-/veroviz/models/wedge_black.gltf'] = {
    label : 'wedge_1 (/veroviz/models/wedge_black.gltf)', 
    childModels : ['o-wedge_1-/veroviz/models/wedge_black.gltf-move'],
    scale : 75, 
    minPxSize : 50 
}; 
objectInfo['wedge_2-/veroviz/models/wedge_white.gltf'] = {
    label : 'wedge_2 (/veroviz/models/wedge_white.gltf)', 
    childModels : ['o-wedge_2-/veroviz/models/wedge_white.gltf-move'],
    scale : 75, 
    minPxSize : 50 
}; 
    registerObjects(objectInfo); 
}