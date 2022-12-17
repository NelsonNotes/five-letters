import { TSessionResponse } from '../../types/session'

export const sessionPull = (): TSessionResponse | null => {
	const session = localStorage.getItem('session')
	return session ? (JSON.parse(session) as TSessionResponse) : null
}

export const sessionPush = (session: TSessionResponse): void =>
	localStorage.setItem('session', JSON.stringify(session))

export const sessionFlush = () => {
	localStorage.clear()
}
