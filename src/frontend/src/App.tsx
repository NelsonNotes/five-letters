import { useEffect, useState } from 'react'
import { useAppDispatch } from './hooks/app'
import { useSelector } from 'react-redux'

import gameLogo from './assets/logo.svg'
import './App.css'
import { selectUser } from './store/user/selectors'
import { fetchUser } from './store/user/actions'
import { fetchSession } from './store/session/actions'
import { makeAttempt } from './store/attempt/actions'
import { selectAttempt } from './store/attempt/selectors'
import { selectSession } from './store/session/selectors'

export const App = () => {
	const dispatch = useAppDispatch()

	const [count, setCount] = useState(0)

	const user = useSelector(selectUser)
	const attempt = useSelector(selectAttempt)
	const session = useSelector(selectSession)

	useEffect(() => {
		if (count === 1) {
			console.log('NELSON session', session)
		}
		if (count === 2) {
			dispatch(
				fetchSession({
					grant_type: 'password',
					username: 'nikitazharov2',
					password: 'NikitaNelson2002',
				})
			)
		}
		if (count === 3) {
			dispatch(fetchUser())
		}
		if (count === 4) {
			dispatch(makeAttempt({ attempt: 'попыт' }))
		}
	}, [count])

	useEffect(() => {
		console.log('NELSON user', user)
	}, [user])

	useEffect(() => {
		console.log('NELSON attempt', attempt)
	}, [attempt])

	useEffect(() => {
		console.log('NELSON session', session)
	}, [session])

	return (
		<div className='App'>
			<div>
				<img src={gameLogo} className='logo' alt='Game logo' />
			</div>
			<h1>Загрузка . . .</h1>
			<div className='card'>
				<button onClick={() => setCount((count) => count + 1)}>
					Вы накликали {count} раз
				</button>
			</div>
			<p className='read-the-docs'>Пока можно потыкать счетчик</p>
		</div>
	)
}
