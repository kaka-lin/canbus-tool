WorkerScript.onMessage = function(msg) {
    //console.log(JSON.stringify(msg))
    if (Object.keys(msg).length === 1) {
        msg.model.clear();
        msg.model.sync();
    } else {
        var data = {'time': msg.time, 'can_id': msg.can_id, 'dlc': msg.dlc, 'data': msg.data};
        console.log("test")

        msg.model.append(data);
        msg.model.sync();
    }
}
