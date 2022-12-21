import { globalConsts } from '../constants'
import { sessionPull } from '../store/session/utils'

export async function customFetch<R = any, B = any>(
	uri: string,
	method: 'GET' | 'POST',
	body?: B,
	asFormData: boolean = false
): Promise<R> {
	let headers = new Headers()

	headers.append('Accept', 'application/json')

	headers.append('Access-Control-Allow-Origin', globalConsts.SRC_URL)
	headers.append('Access-Control-Allow-Credentials', 'true')

	const session = sessionPull()

	if (session) {
		headers.append(
			'Authorization',
			`${session.token_type} ${session.access_token}`
		)
	}

	if (method === 'GET') {
		const result = await fetch(globalConsts.API_URL + uri, {
			// credentials: 'include',
			method,
			headers: headers,
		})
		return result.json()
	}

	// let formData: FormData = new FormData()
	let formData = ''

	if (asFormData && body) {
		// Object.keys(body).forEach((key) => formData.append(key, (body as any)[key]))
		Object.keys(body).forEach(
			(key) => (formData += `${key}=${(body as any)[key]}&`)
		)
		headers.append('Content-Type', 'application/x-www-form-urlencoded')
	} else {
		headers.append('Content-Type', 'application/json')
	}

	const result = await fetch(globalConsts.API_URL + uri, {
		// credentials: 'include',
		method,
		body: asFormData && formData ? formData : JSON.stringify(body),
		headers,
	})

	if (!result.ok) {
		return result.text().then((text) => {
			throw new Error(text)
		})
	}

	return result.json()
}
