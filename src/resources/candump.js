WorkerScript.onMessage = function(msg) {
    var data = {'time': msg.time, 'can_id': msg.can_id, 'dlc': msg.dlc, 'data': msg.data};
    msg.model.append(data);
    msg.model.sync();
}
