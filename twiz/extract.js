import { exists, createReadStream } from 'fs'
import { Extract } from 'unzip'

module.exports = async function extract(src, sink) {
    const _yes = await exists(src)
    if (!_yes) {
        return false;
    }

    createReadStream(src, { mode: 'r', autoClose: true })
        .pipe(Extract({ path: sink })).on('close', () => {
            return true
        })

}